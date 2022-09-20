import { Button, DatePicker, Form, Input, InputNumber, Select } from "antd";
import { RangePickerProps } from "antd/lib/date-picker";
import moment from "moment";
import React from "react";

const { Option } = Select;
const { RangePicker } = DatePicker;
const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const EventForm: React.FC = () => {
  const [form] = Form.useForm();

  const onFinish = (values: any) => {
    console.log(values);
  };

  const onReset = () => {
    form.resetFields();
  };
  // eslint-disable-next-line arrow-body-style
  const disabledDate: RangePickerProps["disabledDate"] = (current) => {
    // Can not select days before today and today
    return current < moment().startOf("day");
  };

  return (
    <Form {...layout} form={form} name="control-hooks" onFinish={onFinish}>
      <Form.Item
        name="eventName"
        label="イベント名"
        rules={[{ required: true }]}
      >
        <Input size="large" showCount maxLength={100} />
      </Form.Item>
      <Form.Item name="timeRange" label="イベント日時">
        <RangePicker size="large" disabledDate={disabledDate} showTime />
      </Form.Item>
      <Form.Item name="category" label="カテゴリ">
        <Select size="large">
          <Option value="sample">サンプル</Option>
        </Select>
      </Form.Item>
      <Form.Item name="limitsParticipants" label="参加上限人数">
        <InputNumber size="large" />
      </Form.Item>
      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
        <Button htmlType="button" onClick={onReset}>
          Reset
        </Button>
      </Form.Item>
    </Form>
  );
};

export default EventForm;
