import { createSlice } from "@reduxjs/toolkit";

const importedDataStore = createSlice({
  name: 'importedData',
  initialState: [],
  reducers: {
    setImportedData: (state, action) => {
      return action.payload;
    }
  }
});

export const { setImportedData } = importedDataStore.actions;
export default importedDataStore.reducer;