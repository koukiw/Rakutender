import {
    UserOutlined,
    ToolOutlined,
    CommentOutlined,
    CarryOutOutlined,
} from '@ant-design/icons';
import type { MenuProps } from 'antd';
import { Menu } from 'antd';
import React, { useState } from 'react';

type MenuItem = Required<MenuProps>['items'][number];

function getItem(
    label: React.ReactNode,
    key: React.Key,
    icon?: React.ReactNode,
    children?: MenuItem[],
    type?: 'group',
): MenuItem {
    return {
        key,
        icon,
        children,
        label,
        type,
    } as MenuItem;
}

const items: MenuItem[] = [
    getItem('募集一覧', '1', <CommentOutlined />),
    getItem('参加予定一覧', '2', <CarryOutOutlined />),
    getItem('マイページ', '3', <UserOutlined />),
    getItem('設定', '4', <ToolOutlined />),
];

const Sidebar: React.FC = () => {
    const [collapsed, setCollapsed] = useState(false);

    const toggleCollapsed = () => {
        setCollapsed(!collapsed);
    };

    return (
        <>
            <div className="logo" />
            <Menu
                defaultSelectedKeys={['1']}
                mode="inline"
                theme="dark"
                inlineCollapsed={collapsed}
                items={items}
            />
        </>
    );
};

export default Sidebar;