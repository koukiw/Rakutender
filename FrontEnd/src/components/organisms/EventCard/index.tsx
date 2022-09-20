import { Card } from "antd";
import EventTitle from "components/atoms/Text/EventTitle";
import EventText from "components/atoms/Text/EventTitle";
import { format } from "date-fns";
import React from "react";

const EventCard: React.FC<{
  title: string;
  date: Date;
  category: string;
  people: number;
}> = ({ title, date, category, people }) => (
  <>
    <Card
      title={<EventTitle content={title} />}
      extra={<a href="#">参加</a>}
      style={{ width: "100vh" }}
    >
      <p>
        <EventText content={"日時　　：　　" + format(date, "MM月dd日")} />
      </p>
      <p>
        <EventText content={"カテゴリ：　　" + category} />
      </p>
      <p>
        <EventText content={"人数　　：　　" + String(people)} />
      </p>
    </Card>
  </>
);

export default EventCard;
