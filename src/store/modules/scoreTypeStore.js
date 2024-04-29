import { createSlice } from "@reduxjs/toolkit";

// interface ScoreTypeState {
//   quiz: any[];
//   assignment: any[];
//   exam: any[];
//   attendance: any[];
// }

// const initialState: ScoreTypeState = {
//   quiz: [],
//   assignment: [],
//   exam: [],
//   attendance: []
// };

// const initialState: ScoreTypeState = {
//   quiz: null,
//   assignment: null,
//   exam: null,
//   attendance: null
// };

const scoreTypeStore = createSlice({
  name: 'scoreType',
  initialState:{
      quiz: null,
      assignment: null,
      exam: null,
      attendance: null
    },
  reducers: {
    setScoreType: (state, action) => {
      switch (action.payload.type) {
        case 'quiz':
          state.quiz = [...state.quiz, action.payload.data];
          break;
        case 'assignment':
          state.assignment = [...state.assignment, action.payload.data];
          break;
        case 'exam':
          state.exam = [...state.exam, action.payload.data];
          break;
        case 'attendance':
          state.attendance = [...state.attendance, action.payload.data];
          break;
        default:
          break;
      }    }
  }
});

export const { setScoreType } = scoreTypeStore.actions;
export default scoreTypeStore.reducer;
