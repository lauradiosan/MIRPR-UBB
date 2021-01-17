import {Component} from '@angular/core';
import {HolidayRequest} from './domain/holiday-request';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  baseUrl = 'http://jderu.cf:8080/holiday-request';
  budget: number;
  picture: any;
  minBedrooms: number;
  description = '';
  city = '';
  response: any[];

  constructor(private readonly httpClient: HttpClient) {
  }


  send(): void {
    const holiday = new HolidayRequest();
    this.getHoliday(holiday);
    console.log(holiday);
    this.httpClient.post<any[]>(this.baseUrl, holiday, httpOptions)
      .subscribe(
        response => this.response = response,
        error => console.log(error)
      );

  }

  getHoliday(holiday: HolidayRequest): void {
    holiday.budget = this.budget;
    holiday.city = this.city;
    holiday.description = this.description;
    holiday.minBedrooms = this.minBedrooms;
    holiday.picture = this.picture;
  }

  goToAirbnb(url: string): void {
    window.open(url, '_blank');
  }

  onFileChanged(event) {
    const file = event.target.files[0] as File;
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      const img = reader.result.toString().replace(/^data:image\/(png|jpg|jpeg);base64,/, '');
      console.log(img);
      this.picture = img;
    };
  }
}

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  })
};

