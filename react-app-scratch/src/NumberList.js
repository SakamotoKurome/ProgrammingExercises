import React from "react";

function ListItem(props) {
    return <li>{props.value}</li>;
}

function NumberList(props) {
  const numbers = props.numbers;
  return (
    <ul>
      {numbers.map((number) =>
        <ListItem key={number.toString()}
                  value={number} />
      )}
    </ul>
  );
}

const numbers = [1, 2, 3, 4, 5];

export default () => <NumberList numbers={numbers} />
