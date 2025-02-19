import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';

const assignmentsData = {
    "Alice": ["AI Project Report", "Neural Networks Implementation", "Machine Learning Model"],
    "Bob": ["Deep Learning Research", "Python Data Science", "AI Ethics"],
    "Charlie": ["TensorFlow Basics", "Advanced PyTorch", "AI Model Optimization"],
    "David": ["React Portfolio", "Next.js Blog", "Fullstack Project"],
    "Emma": ["UI/UX Design", "Frontend Animations", "Web Security Best Practices"],
    "Frank": ["Angular Dashboard", "Node.js API", "GraphQL Implementation"],
    "Grace": ["Cybersecurity Fundamentals", "Ethical Hacking Basics", "Network Security"],
    "Henry": ["Penetration Testing", "Malware Analysis", "Forensics Investigation"],
    "Jack": ["AWS Cloud Deployment", "Azure DevOps", "Serverless Computing"],
    "Karen": ["Big Data Analysis", "Machine Learning with Pandas", "SQL Optimization"]
};

const Assignment = () => {
    const { studentName } = useParams();
    const navigate = useNavigate();

    const assignments = assignmentsData[decodeURIComponent(studentName)] || ["No assignments available"];

    return (
        <div className="p-8 bg-orange-50 min-h-screen flex flex-col items-center">
            <h1 className="text-4xl font-extrabold text-orange-600 mb-6 border-b-4 border-orange-400 pb-2">{studentName}'s Assignments</h1>

            <button 
                onClick={() => navigate(-1)} 
                className="flex items-center gap-2 mb-6 px-4 py-2 bg-orange-500 text-white font-semibold rounded-lg shadow-md hover:bg-orange-600 transition duration-300"
            >
                <ArrowLeft size={20} /> Back
            </button>

            <div className="w-full max-w-3xl bg-white p-6 rounded-lg shadow-lg border border-orange-300">
                <h2 className="text-2xl font-bold text-orange-700 mb-4">Assignments</h2>
                <ul className="divide-y divide-orange-300">
                    {assignments.map((assignment, index) => (
                        <li 
                            key={index} 
                            className="py-3 text-lg font-medium text-gray-800 hover:text-orange-600 transition duration-200"
                        >
                            {index + 1}. {assignment}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Assignment;
