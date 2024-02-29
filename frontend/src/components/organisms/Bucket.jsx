import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import MediaCardList from './MediaCardList';
import KeywordCardList from './KeywordCardList';
import ContentCardList from './ContentCardList';

function CustomTabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

CustomTabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

export default function BasicTabs() {
  const producerCardDatas = [
    { img: "url", title: "대한민국 명산 도전", url: "url" },
    { img: "url", title: "램블러", url: "url" },
    { img: "url", title: "놀자", url: "url" },
    { img: "url", title: "길잡이", url: "url" },
  ]; //API

  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
          <Tab                          
          sx={{    
            px: 1,                              
            fontSize: '16px',                
            fontWeight: 'normal',                 
          }}                                    
          label="매체" {...a11yProps(0)} />
          <Tab 
          sx={{    
            px: 1,                              
            fontSize: '16px',                
            fontWeight: 'normal',                 
          }}    
          label="키워드" {...a11yProps(1)} />
          <Tab 
          sx={{    
            px: 1,                              
            fontSize: '16px',                
            fontWeight: 'normal',                 
          }}    
          label="컨텐츠" {...a11yProps(2)} />
        </Tabs>
      </Box>
      <CustomTabPanel value={value} index={0}>
        <MediaCardList></MediaCardList>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <KeywordCardList></KeywordCardList>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={2}>
        <ContentCardList></ContentCardList>
      </CustomTabPanel>
    </Box>
  );
}