import { createSlice } from "@reduxjs/toolkit";


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
      return action.payload;

      // switch (action.payload.type) {
      //   case 'quiz':
      //     state.quiz = [...state.quiz, action.payload.data];
      //     break;
      //   case 'assignment':
      //     state.assignment = [...state.assignment, action.payload.data];
      //     break;
      //   case 'exam':
      //     state.exam = [...state.exam, action.payload.data];
      //     break;
      //   case 'attendance':
      //     state.attendance = [...state.attendance, action.payload.data];
      //     break;
      //   default:
      //     break;
      // }    
    }
  }
});

export const { setScoreType } = scoreTypeStore.actions;
export default scoreTypeStore.reducer;
