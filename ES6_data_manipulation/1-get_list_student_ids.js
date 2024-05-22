function getListStudentIds(arrayOfObjects) {
  if (!Array.isArray(arrayOfObjects)) {
    return [];
  }
  const studentIds = arrayOfObjects.map((student) => student.id);
  return studentIds;
}

export default getListStudentIds;
