import React from "react";
import styled from "styled-components";

const Container = styled.button`
  width: ${(props) => props.width || "100px"};
  height: ${(props) => props.height || "50px"};
  background-color: ${(props) => props.backgroundColor || "blue"};
  border: ${(props) => (props.border ? props.border : "none")};
  color: ${(props) => props.textColor || "white"};
  font-size: ${(props) => props.fontSize || "16px"};
  border-radius: 4px;
`;

function makeButton({
  width,
  height,
  backgroundColor,
  border,
  textColor,
  fontSize,
  onClick,
  children,
}) {
  return (
    <Container
      width={width}
      height={height}
      backgroundColor={backgroundColor}
      border={border}
      textColor={textColor}
      fontSize={fontSize}
      onClick={onClick}
    >
      {children}
    </Container>
  );
}

export default makeButton;
