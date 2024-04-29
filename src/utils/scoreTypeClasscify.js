// utils/scoreTypeClassify.js
export function classifyColumnLabels(columnLabels) {
    const scoreTypes = {
      quiz: [],
      exam: [],
      assignment: [],
      attendance: []
    };
  
    columnLabels.forEach(label => {
      if (label.includes('Quiz:')) {
        const quizName = label.split('Quiz:')[1].trim();
        scoreTypes.quiz.push({ name: quizName });
      } else if (label.includes('Exam:')) {
        const examName = label.split('Exam:')[1].trim();
        scoreTypes.exam.push({ name: examName });
      } else if (label.includes('Assignment:')) {
        const assignmentName = label.split('Assignment:')[1].trim();
        scoreTypes.assignment.push({ name: assignmentName });
      } else if (label.includes('Attendance:')) {
        const attendanceName = label.split('Attendance:')[1].trim();
        scoreTypes.attendance.push({ name: attendanceName });
      }
    });
  
    return scoreTypes;
  }

  export default classifyColumnLabels