import { error } from '@sveltejs/kit';
import ChartService from '../../../../services/chartService.js';
import FilterOptions from '../../../../models/filterOptions.js'
let service = new ChartService(); 
let selectedFilterOptions = new FilterOptions();
selectedFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];

export async function load({ params }) {
    selectedFilterOptions.legislature = params.legislature;
    selectedFilterOptions.meetingNumber = parseInt(params.meetingNumber); 
    const legislatureAndMeetingsPromise = service.getLegislaturesAndMeetings();
	const chartDataPromise = service.fetchSpeechTypes(selectedFilterOptions);
    const [legislatureAndMeetings, chartData] = await Promise.all([legislatureAndMeetingsPromise, chartDataPromise]);
    return {
        legislatureAndMeetings: structuredClone(legislatureAndMeetings), // clones are needed for ssr only rendered data see https://www.okupter.com/blog/sveltekit-cannot-stringify-arbitrary-non-pojos-error 
        selectedFilterOptions: structuredClone(selectedFilterOptions),
        chartData: structuredClone(chartData)
    };
}