import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HouseTableComponent } from './house/house-table/house-table.component';
import { HouseFormComponent } from './house/house-form/house-form.component';

const routes: Routes = [
  { path: '', redirectTo: 'houses', pathMatch: 'full' },
  { path: 'houses', component: HouseTableComponent },
  { path: 'houses/register', component: HouseFormComponent },
  { path: 'houses/:id/edit', component: HouseFormComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
