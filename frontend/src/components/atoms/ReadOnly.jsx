import * as React from 'react';
import TextField from '@mui/material/TextField';
import styled from 'styled-components';

const Container = styled.div`
  width:220px;
  height:48px;
  margin-top: 20px;
  margin-bottom: 25px;
`;

export default function FormPropsTextFields({label, defaultValue}) {
    return (
        <Container>
          <TextField
            id="standard-read-only-input"
            label={label}
            defaultValue={defaultValue}
            InputProps={{
              readOnly: true,
            }}
            variant="standard"
            focused
          />
        </Container>
    );
  }