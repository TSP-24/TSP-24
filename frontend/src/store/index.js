import { configureStore } from '@reduxjs/toolkit';
import importedDataReducer from './modules/importedDataStore';

const store = configureStore({
  reducer: {
    importedData: importedDataReducer,
  },
});

export default store;