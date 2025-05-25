import React, { useEffect, useState } from 'react';
import { fetchPrograms } from '../api/programs';
import ProgramCard from '../components/ProgramCard';

const Home = () => {
  const [programs, setPrograms] = useState([]);

  useEffect(() => {
    fetchPrograms().then(data => setPrograms(data.results));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-6 text-center">Оберіть програму</h1>
      <div className="grid grid-cols-1 gap-4">
        {programs.map(program => (
          <ProgramCard key={program.id} program={program} />
        ))}
      </div>
    </div>
  );
};

export default Home;