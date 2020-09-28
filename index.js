"use strict";

const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const ipcMain = electron.ipcMain;

// やること
// 設定(常に下、更新スピード)

let mainWindow = null;

app.on("window-all-closed", () => {
  if (process.platform != "darwin") {
    app.quit();
  }
});

app.on("ready", () => {
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 800,
    frame: false,
    resizable: false,
    transparent: true,
    hasShadow: false, //変わらん
    // skipTaskbar: false, //タスクバーに表示するか
    webPreferences: {
      nodeIntegration: true,
    },
    useContentSize: false, // わからん
    maximazable: false,
    fullscreenable: false,
    icon: `${__dirname}/assets/pics/tareopen.png`,
  });
  mainWindow.loadURL(`file://${__dirname}/assets/main.html`);

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
  // サイズ変更拒否
  mainWindow.setFullScreenable(false);
  mainWindow.setMaximizable(false);
  mainWindow.isResizable(false);

  ipcMain.on('close-message', (event, arg) => {
    mainWindow = null;
    app.quit();
  });
});
