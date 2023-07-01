import { error } from '@sveltejs/kit';
import ChartService from './../../../../../services/chartService.js';
import FilterOptions from './../../../../../models/filterOptions.js'
let service = new ChartService(); 
let selectedFilterOptions = new FilterOptions();
selectedFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];

export async function load({ params }) {
    selectedFilterOptions.legislature = params.legislature;
    selectedFilterOptions.meetingNumber = parseInt(params.meetingNumber); 
    selectedFilterOptions.topic = {topic: params.topic};
    const legislatureAndMeetingsPromise = service.getLegislaturesAndMeetings();
	const chartDataPromise = service.fetchSpeechTypes(selectedFilterOptions);
    const [legislatureAndMeetings, chartData] = await Promise.all([legislatureAndMeetingsPromise, chartDataPromise]);

    if (!legislatureAndMeetings.filter(x => x.legislature == selectedFilterOptions.legislature)[0]?.meetings.includes(selectedFilterOptions.meetingNumber)) {        
        throw error(404, 'Not found');
    }
    return {
        legislatureAndMeetings: structuredClone(legislatureAndMeetings), // clones are needed for ssr only rendered data see https://www.okupter.com/blog/sveltekit-cannot-stringify-arbitrary-non-pojos-error 
        selectedFilterOptions: structuredClone(selectedFilterOptions),
        chartData: structuredClone(chartData)
    };
}