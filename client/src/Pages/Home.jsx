import React from 'react';
import { useNavigate } from 'react-router-dom';

const organizations = [
    { name: 'Neural Nexus', domain: 'AI & Machine Learning', software: 'TensorFlow, PyTorch' },
    { name: 'Code Crafters', domain: 'Web Development', software: 'React, Angular' },
    { name: 'Cyber Shield', domain: 'Cybersecurity', software: 'Wireshark, Metasploit' },
    { name: 'Cloud Haven', domain: 'Cloud Computing', software: 'AWS, Azure' },
    { name: 'Data Wizards', domain: 'Data Science', software: 'Pandas, NumPy' },
    { name: 'App Innovators', domain: 'Mobile Development', software: 'Flutter, Swift' }
];

const Home = () => {
    const navigate = useNavigate();

    const handleClick = (orgName) => {
        navigate(`/students/${encodeURIComponent(orgName)}`);
    };

    return (
        <div className="p-8 bg-gray-100 min-h-screen">
            <h1 className="text-4xl font-extrabold text-center text-orange-600 mb-8">Organizations</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 cursor-pointer">
                {organizations.map((org, index) => (
                    <div 
                        key={index} 
                        className="p-6 bg-white border border-orange-400 rounded-lg shadow-lg transform hover:scale-105 transition duration-300"
                        onClick={() => handleClick(org.name)}
                    >
                        <h2 className="text-2xl font-bold text-orange-700 mb-2">{org.name}</h2>
                        <p className="text-gray-700 font-medium">Domain: <span className="font-semibold">{org.domain}</span></p>
                        <p className="text-gray-700 font-medium">Software: <span className="font-semibold">{org.software}</span></p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Home;
