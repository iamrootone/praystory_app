const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');  // Python 스크립트 실행을 위한 child_process 추가
const fs = require('fs');  // 파일 시스템 접근 모듈

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      enableRemoteModule: false
    },
  });

  win.loadFile('index.html');
}

ipcMain.on('file-upload', (event, fileData) => {
    const { fileContent, year, month, fileName } = fileData;

    const tempDir = app.getPath('temp');
    const tempCsvPath = path.join(tempDir, 'temp.csv');  
    fs.writeFileSync(tempCsvPath, fileContent);

    const resourcePath = "." // 로컬 테스트 용
    // const resourcePath = path.join(process.resourcesPath, 'app.asar.unpacked') // 배포용

    const pythonExecutable = process.platform === 'win32'
        ? path.join(resourcePath, 'resources', 'venv_win', 'Scripts', 'python.exe')
        : path.join(resourcePath, 'resources', 'venv_mac', 'bin', 'python');

    const pythonScript = path.join(resourcePath, 'resources', 'function', 'main.py');  
    const xmlOutputPath = path.join(tempDir, `${year}년_${month}월_기도이야기.xml`);  
    const xslFormatPath = path.join(resourcePath, 'resources', 'function', 'praystory_format.xsl');  

    exec(`"${pythonExecutable}" "${pythonScript}" "${tempCsvPath}" "${xmlOutputPath}" "${xslFormatPath}" ${year} ${month}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing Python script: ${error.message}`);
            event.sender.send('conversion-complete', {
                success: false,
                message: '변환 실패',
                warnings: parseOutput(stderr || stdout),  // 파싱된 출력
            });
            return;
        }

        if (fs.existsSync(xmlOutputPath)) {
            event.sender.send('conversion-complete', {
                success: true,
                message: '변환 완료',
                xmlPath: xmlOutputPath,
                xslPath: xmlOutputPath.substring(0, xmlOutputPath.length - 3) + 'xsl',
                warnings: parseOutput(stderr || stdout),  // 파싱된 출력
            });
        } else {
            event.sender.send('conversion-complete', {
                success: false,
                message: 'XML 또는 XSL 파일 생성 실패',
                warnings: parseOutput(stderr || stdout),  // 파싱된 출력
            });
        }
    });
});

function parseOutput(output) {
    return output.split('\n').map(line => {
        if (line.includes('[INFO_1]')) {
            return { type: 'info1', message: line.replace('[INFO_1]', '') };
        } else if (line.includes('[INFO_2]')) {
          return { type: 'info2', message: line.replace('[INFO_2]', '') };
        } else if (line.includes('[INFO_3]')) {
          return { type: 'info3', message: line.replace('[INFO_3]', '') };
        } else if (line.includes('[WARNING]')) {
            return { type: 'warning', message: line.replace('[WARNING]', '').trim().replace(/\n/g, '<br>') };
        } else if (line.includes('[INFO]')) {
            return { type: 'info', message: line.replace('[INFO]', '').trim().replace(/\n/g, '<br>') };
        } else {
            return { type: 'info', message: line.trim().replace(/\n/g, '<br>') };  // 기본적으로 info로 처리
        }
    });
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
