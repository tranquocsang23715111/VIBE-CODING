import React, { useEffect, useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:8000/students";
const STATS_API = "http://127.0.0.1:8000/stats";

function App() {
  const [students, setStudents] = useState([]);
  const [editing, setEditing] = useState(false);

  const [search, setSearch] = useState("");

  const [totalStudents, setTotalStudents] = useState(0);
  const [avgGPA, setAvgGPA] = useState(0);
  const [majorStats, setMajorStats] = useState([]); // thêm thống kê ngành

  const [form, setForm] = useState({
    student_id: "",
    name: "",
    birth_year: "",
    major: "",
    gpa: ""
  });

  const fetchStudents = async () => {
    const res = await fetch(API);
    const data = await res.json();
    setStudents(data);
  };

  const fetchStats = async () => {
    const totalRes = await fetch(`${STATS_API}/total_students`);
    const totalData = await totalRes.json();

    const avgRes = await fetch(`${STATS_API}/avg_gpa`);
    const avgData = await avgRes.json();

    const majorRes = await fetch(`${STATS_API}/by_major`);
    const majorData = await majorRes.json();

    setTotalStudents(totalData.total_students);
    setAvgGPA(avgData.average_gpa);
    setMajorStats(majorData);
  };

  useEffect(() => {
    fetchStudents();
    fetchStats();
  }, []);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const resetForm = () => {
    setForm({
      student_id: "",
      name: "",
      birth_year: "",
      major: "",
      gpa: ""
    });
    setEditing(false);
  };

  const addStudent = async () => {
    await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    });

    fetchStudents();
    fetchStats();
    resetForm();
  };

  const deleteStudent = async (id) => {
    await fetch(`${API}/${id}`, {
      method: "DELETE"
    });

    fetchStudents();
    fetchStats();
  };

  const startEdit = (student) => {
    setForm(student);
    setEditing(true);
  };

  const updateStudent = async () => {
    await fetch(`${API}/${form.student_id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    });

    fetchStudents();
    fetchStats();
    resetForm();
  };

  const exportCSV = () => {
    window.open("http://127.0.0.1:8000/export/csv");
  };

  const filteredStudents = students.filter((s) =>
    s.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h1>Student Management</h1>

      <button onClick={exportCSV}>Export CSV</button>

      <h2>Statistics</h2>
      <p>Total Students: {totalStudents}</p>
      <p>Average GPA: {avgGPA?.toFixed(2)}</p>

      <h3>Students by Major</h3>
      <table>
        <thead>
          <tr>
            <th>Major</th>
            <th>Total Students</th>
          </tr>
        </thead>
        <tbody>
          {majorStats.map((m, index) => (
            <tr key={index}>
              <td>{m.major}</td>
              <td>{m.total}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Search Student</h2>
      <input
        placeholder="Search by name..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <div className="form">
        <input
          name="student_id"
          placeholder="ID"
          value={form.student_id}
          onChange={handleChange}
          disabled={editing}
        />

        <input
          name="name"
          placeholder="Name"
          value={form.name}
          onChange={handleChange}
        />

        <input
          name="birth_year"
          placeholder="Birth Year"
          value={form.birth_year}
          onChange={handleChange}
        />

        <input
          name="major"
          placeholder="Major"
          value={form.major}
          onChange={handleChange}
        />

        <input
          name="gpa"
          placeholder="GPA"
          value={form.gpa}
          onChange={handleChange}
        />

        {editing ? (
          <>
            <button onClick={updateStudent}>Update Student</button>
            <button onClick={resetForm}>Cancel</button>
          </>
        ) : (
          <button onClick={addStudent}>Add Student</button>
        )}
      </div>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Birth Year</th>
            <th>Major</th>
            <th>GPA</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {filteredStudents.map((s) => (
            <tr key={s.student_id}>
              <td>{s.student_id}</td>
              <td>{s.name}</td>
              <td>{s.birth_year}</td>
              <td>{s.major}</td>
              <td>{s.gpa}</td>
              <td>
                <button onClick={() => startEdit(s)}>Edit</button>
                <button onClick={() => deleteStudent(s.student_id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;