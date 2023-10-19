import { error } from '@sveltejs/kit';
import ChartService from '../../../services/chartService.js';
let service = new ChartService(); 

export async function load({ params, url }) {
    let selectedYear = params.year;
	const chartData = await service.fetchNationalCouncilMeetingDistribution(selectedYear);

    return {
        selectedYear: parseInt(selectedYear), // ATTENTION! we need to parse the value so that two-way binding works!!! event though route param is defined as int, it is no auto-cast done automatically!!!!!
        chartData: chartData
    };
}