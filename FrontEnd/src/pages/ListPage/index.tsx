import { Layout, Space } from "antd";
import PageTitle from "components/atoms/Text/PageTitle";
import EventCard from "components/organisms/EventCard";
import Sidebar from "components/organisms/Sidebar";
import React, { useState } from "react";

const { Header, Content, Footer, Sider } = Layout;

const ListPage: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={(value) => setCollapsed(value)}
      >
        <Sidebar />
      </Sider>

      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 15 }}>
          <PageTitle content="参加予定一覧" />
        </Header>

        <Content style={{ margin: "0 16px" }}>
          <div
            className="site-layout-background"
            style={{ padding: 24, minHeight: 360 }}
          >
            <Space
              direction="vertical"
              size="middle"
              style={{ display: "flex" }}
            >
              <EventCard
                title={"〇〇駅のカラオケ行こう！"}
                date={new Date()}
                category={"カラオケ"}
                people={5}
              />
              <EventCard
                title={"2泊3日　▲▲旅行"}
                date={new Date()}
                category={"旅行"}
                people={4}
              />
            </Space>
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default ListPage;
