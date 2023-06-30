import { error } from '@sveltejs/kit';
import ChartService from './../../../../services/chartService.js';
import FilterOptions from './../../../../models/filterOptions.js'
let service = new ChartService(); 

// export const prerender = false;

let selectedFilterOptions = new FilterOptions();
selectedFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];

export async function load({ params }) {
  
    const legislatureAndMeetings = await service.getLegislaturesAndMeetings();
	const chartData = await service.fetchSpeechTypes(selectedFilterOptions);
    
    selectedFilterOptions.legislature = params.legislature;
    selectedFilterOptions.meetingNumber = parseInt(params.meetingNumber); 
    
    return {
        legislatureAndMeetings: structuredClone(legislatureAndMeetings), // clones are needed for ssr only rendered data see https://www.okupter.com/blog/sveltekit-cannot-stringify-arbitrary-non-pojos-error 
        selectedFilterOptions: structuredClone(selectedFilterOptions),
        chartData: structuredClone(chartData)
    };
}