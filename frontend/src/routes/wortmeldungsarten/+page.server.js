import { error } from '@sveltejs/kit';
import ChartService from './../../services/chartService.js';
import FilterOptions from './../../models/filterOptions.js'
let service = new ChartService(); 

export const prerender = true;

let selectedFilterOptions = new FilterOptions();
selectedFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];
let shownFilterOptions = new FilterOptions();

export async function load({ params }) {
  
    const legislatureAndMeetings = await service.getLegislaturesAndMeetings();
    shownFilterOptions = selectedFilterOptions;
	const chartData = await service.fetchSpeechTypes(selectedFilterOptions);
    
    selectedFilterOptions.legislature = legislatureAndMeetings.slice(-1)[0].legislature;
    selectedFilterOptions.meetingNumber = legislatureAndMeetings.slice(-1)[0].meetings.slice(-1)[0];
  
    return {
        legislatureAndMeetings: structuredClone(legislatureAndMeetings), // clones are needed for ssr only rendered data see https://www.okupter.com/blog/sveltekit-cannot-stringify-arbitrary-non-pojos-error 
        selectedFilterOptions: structuredClone(selectedFilterOptions),
        chartData: structuredClone(chartData)
    };
}