import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import "./App.css";
import AppProvider from "provider/app";
import { path } from "constants/path";
import MainPage from "pages/MainPage";
import ChatPage from "pages/ChatPage";
import ListPage from "pages/ListPage";
import SettingPage from "pages/SettingPage";
import MyPage from "pages/MyPage";

function App() {
  return (
    <AppProvider serverHost="http://localhost:8081">
      <BrowserRouter>
        <Routes>
          {PAGE_CONTENTS.map((page) => (
            <Route path={page.path} element={<page.Component />} />
          ))}
        </Routes>
      </BrowserRouter>
    </AppProvider>
  );
}

export const PAGE_CONTENTS: {
  path: string;
  name: string;
  Component: React.FC;
}[] = [
  { path: path.MainPage, name: "ホーム", Component: MainPage },
  { path: path.ListPage, name: "一覧画面", Component: ListPage },
  { path: path.ChatPage, name: "チャット画面", Component: ChatPage },
  { path: path.ChatPage, name: "マイページ", Component: MyPage },
  { path: path.ChatPage, name: "設定画面", Component: SettingPage },
];
export default App;
