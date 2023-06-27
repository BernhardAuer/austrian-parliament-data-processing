import SpeechService from './../../../../services/speechService.js';
let service = new SpeechService();
let speeches = [];
let speechesByTopic = [];
let topics = [];

const groupBy = (x, f) => x.reduce((a, b, i) => ((a[f(b, i, x)] ||= []).push(b), a), {}); // credit: https://stackoverflow.com/questions/14446511/most-efficient-method-to-groupby-on-an-array-of-objects

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    speeches = await service.fetchSpeeches({ legislature: params.legislature, meetingNumber: params.meetingNumber });
    speechesByTopic = groupBy(speeches, (x) => x.topic);
    topics = Object.keys(speechesByTopic);

    return {
        topics: topics,
        speechesByTopic: speechesByTopic
    };
}