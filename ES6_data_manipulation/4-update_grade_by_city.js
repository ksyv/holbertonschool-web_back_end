function updateStudentGradeByCity(students, city, newGrades) {
  const newGradesMap = new Map(newGrades.map(({ studentId, grade }) => [studentId, grade]));
  const updatedStudents = students
    .filter((student) => student.location === city)
    .map((student) => ({
      ...student,
      grade: newGradesMap.has(student.id) ? newGradesMap.get(student.id) : 'N/A',
    }));
  return updatedStudents;
}

export default updateStudentGradeByCity;
