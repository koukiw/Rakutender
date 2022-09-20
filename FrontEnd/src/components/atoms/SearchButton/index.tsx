import { SearchOutlined } from '@ant-design/icons';
import { Button } from 'antd';
import React from 'react';

const SearchButton: React.FC = () => (
    <>
        <Button type="primary" icon={<SearchOutlined />}>
            Search
        </Button>
    </>
);

export default SearchButton;