const { contextBridge, ipcRenderer } = require('electron');

// 렌더러 프로세스에서 메인 프로세스로 안전하게 메시지를 보내는 함수
contextBridge.exposeInMainWorld('api', {
  sendFileData: (fileData) => ipcRenderer.send('file-upload', fileData),
  onConversionComplete: (callback) => ipcRenderer.on('conversion-complete', callback)
});

// Main 프로세스에서 전송한 로그 수신
ipcRenderer.on('log-message', (event, message) => {
  console.log(message); // 개발자 도구 콘솔에 출력
});
