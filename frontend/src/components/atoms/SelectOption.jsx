import * as React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function SelectAutoWidth({ data = [], onSelect, defaultSelect, width = '210px' }) {
  // 내부 상태를 사용하여 선택된 값을 추적합니다.
  const [selectedValue, setSelectedValue] = React.useState(defaultSelect || '');

  React.useEffect(() => {
    // defaultSelect 값이 변경될 때마다, 내부 상태를 업데이트합니다.
    if (defaultSelect !== undefined && defaultSelect !== null) {
      
      setSelectedValue(defaultSelect);
    }
  }, [defaultSelect]);

  // 선택된 값이 변경될 때마다, onSelect 콜백 함수와 내부 상태를 모두 업데이트 합니다.
  const handleChange = (e) => {
    const value = e.target.value;
    // console.log("값 변경 완료",value)
    setSelectedValue(value);
    onSelect(value);
  };

  return (
    <FormControl variant="standard" sx={{ m: 1, minWidth: width }}>
      <InputLabel id="demo-simple-select-standard-label"></InputLabel>
      <Select
        labelId="demo-simple-select-standard-label"
        id="demo-simple-select-standard"
        value={selectedValue}
        onChange={handleChange}
      >
      {
        Array.isArray(data) && data.map((item) => (
          <MenuItem value={item.id} key={item.id}>
            {Object.values(item)[1]}
          </MenuItem>
        ))
      }
      </Select>
    </FormControl>
  );
}
