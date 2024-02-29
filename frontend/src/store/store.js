import { configureStore } from "@reduxjs/toolkit";
import { persistStore } from "redux-persist";

import userReducer from "../slices/userSlice";
import resultReducer from "../slices/resultSlice";

export const store = configureStore({
  reducer: {
    user: userReducer,
    result: resultReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
});

export const persistor = persistStore(store);
