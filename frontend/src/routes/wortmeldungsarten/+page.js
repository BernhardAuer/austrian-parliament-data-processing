import { error } from '@sveltejs/kit';
import ChartService from './../../services/chartService.js';
import FilterOptions from './../../models/filterOptions.js'
let service = new ChartService(); 

let selectedFilterOptions = new FilterOptions();
selectedFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];

export async function load({ params }) {
  
    const legislatureAndMeetings = await service.getLegislaturesAndMeetings();
    
    selectedFilterOptions.legislature = legislatureAndMeetings.slice(-1)[0].legislature;
    selectedFilterOptions.meetingNumber = legislatureAndMeetings.slice(-1)[0].meetings.slice(-1)[0];
  
    return {
        legislatureAndMeetings: legislatureAndMeetings,
        selectedFilterOptions: selectedFilterOptions
    };
}