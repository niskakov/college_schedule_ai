import axios from 'axios';

const API_URL = 'http://localhost:8000';

export interface Schedule {
  id: number;
  course: { id: number; name: string; teacher: { name: string }; group: { name: string } };
  day: string;
  slot: number;
  room: { id: number; name: string };
}

export interface TimetableResponse {
  schedules: Schedule[];
}

export const getTimetable = async (): Promise<TimetableResponse> => {
  const response = await axios.post(`${API_URL}/timetable/generate`);
  return response.data;
};
