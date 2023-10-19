import { error } from '@sveltejs/kit';
import ChartService from '../../../services/chartService.js';
let service = new ChartService(); 

export async function load({ params, url }) {
    let selectedYear = params.year;
	const chartData = await service.fetchNationalCouncilMeetingDistribution(selectedYear);

    return {
        selectedYear: selectedYear,
        chartData: chartData
    };
}