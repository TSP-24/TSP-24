import { configureStore } from '@reduxjs/toolkit';
import importedDataReducer from './modules/importedDataStore';
import scoreTypeReducers from './modules/scoreTypeStore.js';
const store = configureStore({
  reducer: {
    importedData: importedDataReducer,
    scoreType: scoreTypeReducers
    
  },
});

export default store;