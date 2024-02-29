import { createSlice } from "@reduxjs/toolkit";
import { persistReducer } from "redux-persist";
import storageSession from "redux-persist/lib/storage/session";

const initialState = {
  target: {},
  media: {},
  recommendedMedia: null,
  selectedPrice: null,
  selectedOnOffline: null,
  selectedBigRegion: null,
  selectedSmallRegion: null,
  bigRegionName: null,
  smallRegionName: null,
};

const persistConfig = {
  key: "result",
  storage: storageSession,
  whitelist: [
    "target",
    "media",
    "recommendedMedia",
    "selectedPrice",
    "selectedOnOffline",
    "selectedBigRegion",
    "selectedSmallRegion",
    "bigRegionName",
    "smallRegionName",
  ],
};

const resultSlice = createSlice({
  name: "result",
  initialState,
  reducers: {
    setTarget(state, action) {
      state.target = action.payload;
    },
    setMedia(state, action) {
      state.media = action.payload;
      console.log(state.media);
    },
    setRecommendedMedia(state, action) {
      state.recommendedMedia = action.payload;
    },
    setSelectedPrice(state, action) {
      state.selectedPrice = action.payload;
    },
    setSelectedOnOffline(state, action) {
      state.selectedOnOffline = action.payload;
    },
    setSelectedBigRegion(state, action) {
      state.selectedBigRegion = action.payload;
    },
    setSelectedSmallRegion(state, action) {
      state.selectedSmallRegion = action.payload;
    },
    setbigRegionName(state, action) {
      state.bigRegionName = action.payload;
    },
    setsmallRegionName(state, action) {
      state.smallRegionName = action.payload;
    },
  },
});

export const {
  setTarget,
  setMedia,
  setRecommendedMedia,
  setSelectedPrice,
  setSelectedOnOffline,
  setSelectedBigRegion,
  setSelectedSmallRegion,
  setbigRegionName,
  setsmallRegionName,
} = resultSlice.actions;

const persistedReducer = persistReducer(persistConfig, resultSlice.reducer);
export default persistedReducer;
