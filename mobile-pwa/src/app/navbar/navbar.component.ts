import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent {

  constructor(private router: Router) {}

  onCreateAlert() {
    this.router.navigate(['/create-alert']);
  }

  onManageAlerts() {
    this.router.navigate(['/manage-alerts']);
  }
}
