// Angular can work with the response: 3
interface Patient {
  id: number;
  name: string;
  age: number;
}

this.http.get<Patient[]>('/api/patients/')
  .subscribe(patients => {
    console.log(patients);
  });


//   The TypeScript interface describes the expected shape; it does not validate the server response at runtime by itself.