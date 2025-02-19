import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';

const studentsData = {
    "Neural Nexus": ["Alice", "Bob", "Charlie", "Daniel", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "Code Crafters": ["David", "Emma", "Frank", "George", "Hannah", "Isaac", "Julia", "Kevin", "Lily", "Mason"],
    "Cyber Shield": ["Grace", "Henry", "Isla", "Jack", "Karen", "Liam", "Mia", "Nathan", "Olivia", "Paul"],
    "Cloud Haven": ["Jack", "Karen", "Liam", "Mia", "Nathan", "Olivia", "Paul", "Quinn", "Rachel", "Sophia"],
    "Data Wizards": ["Mia", "Nathan", "Olivia", "Paul", "Quinn", "Rachel", "Sophia", "Thomas", "Uma", "Victor"],
    "App Innovators": ["Paul", "Quinn", "Rachel", "Sophia", "Thomas", "Uma", "Victor", "Wendy", "Xavier", "Zoe"]
};

const StudentsList = () => {
    const { orgName } = useParams();
    const navigate = useNavigate();

    const students = studentsData[decodeURIComponent(orgName)] || [];

    const handleStudentClick = (studentName) => {
        navigate(`/students/${encodeURIComponent(orgName)}/${encodeURIComponent(studentName)}`);
    };

    return (
        <div className="p-8 bg-orange-50 min-h-screen flex flex-col items-center">
            <h1 className="text-4xl font-extrabold text-orange-600 mb-6 border-b-4 border-orange-400 pb-2">{orgName} - Students</h1>

            <button 
                onClick={() => navigate(-1)} 
                className="flex items-center gap-2 mb-6 px-4 py-2 bg-orange-500 text-white font-semibold rounded-lg shadow-md hover:bg-orange-600 transition duration-300"
            >
                <ArrowLeft size={20} /> Back
            </button>

            <div className="w-full max-w-3xl bg-white p-6 rounded-lg shadow-lg border border-orange-300">
                <h2 className="text-2xl font-bold text-orange-700 mb-4">Student List</h2>
                <ul className="divide-y divide-orange-300">
                    {students.length > 0 ? (
                        students.map((student, index) => (
                            <li 
                                key={index} 
                                className="py-3 text-lg font-medium text-gray-800 hover:text-orange-600 transition duration-200 cursor-pointer"
                                onClick={() => handleStudentClick(student)}
                            >
                                {index + 1}. {student}
                            </li>
                        ))
                    ) : (
                        <p className="text-red-500 text-center text-lg font-semibold">No students found for this organization.</p>
                    )}
                </ul>
            </div>
        </div>
    );
};

export default StudentsList;
