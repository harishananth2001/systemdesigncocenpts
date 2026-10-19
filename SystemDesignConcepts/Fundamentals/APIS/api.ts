// understanding angular api calls and how to use them in angular components
import { HttpClient } from '@angular/common/http';
import { Component, inject } from '@angular/core';

interface Patient {
  id: number;
  name: string;
  age: number;
  email: string;
}

@Component({
  selector: 'app-patients',
  standalone: true,
  template: `
    <h2>Patients</h2>

    @for (p of patients; track p.id) {
      <p>{{ p.name }} — {{ p.email }}</p>
    }
  `
})
export class PatientsComponent {
  private http = inject(HttpClient);
  patients: Patient[] = [];

  ngOnInit() {
    this.http.get<Patient[]>('/api/patients/')
      .subscribe((data: Patient[]) => this.patients = data);
  }
}