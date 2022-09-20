import { Avatar, Comment, Tooltip } from "antd";
import moment from "moment";
import React, { useState } from "react";

const Message: React.FC<{
  name: string;
  message: string;
  image: string;
  date: string;
}> = ({ name, message, image, date }) => {
  const [] = useState<string | null>(null);

  return (
    <Comment
      author={<a>{name}</a>}
      avatar={<Avatar src={image} alt="Han Solo" />}
      content={<p>{message}</p>}
      datetime={
        <Tooltip title={date}>
          <span>{date}</span>
        </Tooltip>
      }
    />
  );
};

export default Message;
