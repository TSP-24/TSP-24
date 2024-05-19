import { createSlice } from "@reduxjs/toolkit";

const importedDataStore = createSlice({
  name: 'importedData',
  initialState: { scores: [], assessments: [] },
  reducers: {
    setScores: (state, action) => {
      state.scores = action.payload;
    },
    setAssessments: (state, action) => {
      state.assessments = action.payload;
    },
  },
});

export const { setScores, setAssessments } = importedDataStore.actions;
export default importedDataStore.reducer;