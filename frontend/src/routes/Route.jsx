import { Route, Routes } from 'react-router-dom';
import MainPage from '../components/pages/MainPage/MainPage';
import MediaRecommendPage from '../components/pages/MediaRecommendPage/MediaRecommendPage';
import ContentRecommendPage from '../components/pages/ContentRecommendPage/ContentRecommendPage';
import KeywordRecommendPage from '../components/pages/KeywordRecommendPage/KeywordRecommendPage';
import OnlineRecommendation from '../components/pages/OnlineRecommendation/OnlineRecommendation.jsx';
import MyPage from '../components/pages/MyPage/MyPage';
import TvRecommendation from '../components/pages/TvRecommendation/TvRecommendation.jsx';
import RadioRecommendation from '../components/pages/RadioRecommendation/RadioRecommendation.jsx';
import NewspaperRecommendation from '../components/pages/NewspaperRecommendation/NewspaperRecommendation.jsx';
import OutdoorRecommendation from '../components/pages/OutdoorRecommendation/OutdoorRecommendation.jsx';
import Login from '../components/pages/Auth/Login';
import SignPage from '../components/pages/Auth/SignPage';
import PrivateRoute from './PrivateRoute';

function RouteLink(props) {
  return (
    <div>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignPage />} />
        <Route element={<PrivateRoute />}>
          <Route path="/mypage" element={<MyPage />} />
          <Route path="/mediaRecommend" element={<MediaRecommendPage />} />
          <Route path="/mediaResult/online" element={<OnlineRecommendation />} />
          <Route path="/mediaResult/tv" element={<TvRecommendation />} />
          <Route path="/mediaResult/radio" element={<RadioRecommendation />} />
          <Route path="/mediaResult/newspaper" element={<NewspaperRecommendation />} />
          <Route path="/mediaResult/outdoor" element={<OutdoorRecommendation />} />
          <Route path="/keywordRecommend" element={<KeywordRecommendPage />} />
          <Route path="/contentRecommend" element={<ContentRecommendPage />} />
        </Route>
      </Routes>
    </div>
  );
}

export default RouteLink;
