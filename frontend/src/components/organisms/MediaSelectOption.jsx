import React, { useState } from 'react';
import Select from '../atoms/SelectOption';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-between;
  align-items: baseline;
  width: 90%;
  margin-top: 10px;
`;

function MediaSelectOption({
  dataL,
  dataM,
  dataS,
  onSelectL,
  onSelectM,
  onSelectS,
  defaultSelectL,
  defaultSelectM,
  defaultSelectS,
  width
}) {
  const [selectedataL, setSelectedataL] = useState(null);
  const [selectedataM, setSelectedataM] = useState(null);
  const [selectedataS, setSelectedataS] = useState(null);
  return (
    <Container>
      <Select data={dataL || []} onSelect={onSelectL} defaultSelect={defaultSelectL} width={width} />
      <Select data={dataM} onSelect={onSelectM} defaultSelect={defaultSelectM} width={width} />
      <Select data={dataS} onSelect={onSelectS} defaultSelect={defaultSelectS} width={width} />
    </Container>
  );
}

export default MediaSelectOption;
