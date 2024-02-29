import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { store } from './store/store';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import ScrollToTop from './components/atoms/ScrollToTop';

const theme = createTheme({
  palette: {
    primary: {
      main: '#3C486B'
    }
  },
  typography: {
    fontFamily: 'NANUMSQUARENEO-BRG'
  }
});

const root = ReactDOM.createRoot(document.getElementById('root'));
const queryClient = new QueryClient();

root.render(
  <QueryClientProvider client={queryClient}>
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <Provider store={store}>
        <ScrollToTop />
          <App />
        </Provider>
      </ThemeProvider>
    </BrowserRouter>
  </QueryClientProvider>
);

reportWebVitals();
