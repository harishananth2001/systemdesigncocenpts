// service code 
// customer.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CustomerService {
  constructor(private http: HttpClient) {}

  getCustomers(): Observable<any> {
    return this.http.get<any>(
      'http://localhost:8000/api/customers/'
    );
  }
}

// Now measure how long the request takes from Angular.

// customer.component.ts
import { Component } from '@angular/core';
import { CustomerService } from './customer.service';

@Component({
  selector: 'app-customer',
  template: `
    <button (click)="loadCustomers()">
      View Customers
    </button>

    <p>Request time: {{ latency }} ms</p>

    <ul>
      <li *ngFor="let customer of customers">
        {{ customer.name }}
      </li>
    </ul>
  `
})
export class CustomerComponent {
  customers: any[] = [];
  latency = 0;

  constructor(
    private customerService: CustomerService
  ) {}

  loadCustomers(): void {
    const start = performance.now();

    this.customerService.getCustomers().subscribe({
      next: (response) => {
        this.latency = Math.round(
          performance.now() - start
        );

        this.customers = response.customers;

        console.log('Total API duration:', this.latency, 'ms');
        console.log(
          'Server processing:',
          response.server_processing_ms,
          'ms'
        );
      },
      error: (error) => {
        console.error('API request failed:', error);
      }
    });
  }
}