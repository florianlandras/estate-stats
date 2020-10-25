import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {

  public testVar = 'test var ';
  private apiKey = 'https://api.nasa.gov/planetary/apod?api_key=CLHr8Zho80Tr2BcWGkU0w1opiWi01yEwhFRKWZWH'; //TODO never do that
  
  public apodImageUrl: string;
  public apodExplanation: string;
  public apodTitle: string;
  public apodDate: string;
  public apodCopy: string;

  constructor(private http: HttpClient) {
    this.getApodImageUrl();
  }

  /** Function to read API */
  public readApi (url: string) {
    return this.http.get(url);
  }

  /** function use to get url of picture of the day */
  public getApodImageUrl () {
    if (!this.apodImageUrl) { // if doesnt exist yet , get from NASA API
      //read Api
      this.readApi(this.apiKey)
      .subscribe((data) => {
        console.log(data);
        this.apodImageUrl = data['url'];
        this.apodExplanation = data['explanation'];
        this.apodTitle = data['title'];
        this.apodDate = data['date'];
        this.apodCopy = data['copyright'];
      });
    }
  }

}
