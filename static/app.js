const $poolGrids = $('.pool-grid');
const $scheduleGrids = $('.schedule-grid');
const $resultsButton = $('#results-nav');
const $resultsDisplay = $('#results');
const $standingsButton = $('#standings-nav');
const $semifinalsButton = $('#semifinals-nav');
const $finalsButton = $('#finals-nav');
const $standingsDisplay = $('#standings');
const $semifinalsDisplay = $('#semifinals');
const $finalsDisplay = $('#finals');
const $thisWeekButton = $('#this-week-nav');
const $thisWeekDisplay = $('#this-week');
const $scheduleButton = $('#schedule-nav');
const $scheduleDisplay = $('#schedule');
const $scheduleGameButton = $('.schedule-button');
const $schedulerForm = $('#scheduler-form');
const $reportForm = $('#report-form');
const $reportGameButton = $('.report-button');
const $adminLoginButton = $('#admin-login-button');
const $adminLoginForm = $('#admin-login');
const $loginCancel = $('#login-cancel');
const $resultForm = $('#result-form');
const $resultButton = $('.result-button');
const $scoreForm = $('#score-form');
const $scoreButton = $('.score-button');
const $widthSetter = $('#width-setter');
const $playoffRows = $('.playoff-row');

// const BASE_URL = 'http://127.0.0.1:5000';
const BASE_URL = 'https://chess-tournament-organizer.herokuapp.com';

if (window.innerWidth <= 550) {
    $poolGrids.addClass('col-12');
    $poolGrids.removeClass('col-6');

    $scheduleGrids.addClass('col-12');
    $scheduleGrids.removeClass('col-6');
}
$playoffRows.width($widthSetter.width());
$standingsDisplay.hide();

$resultsButton.on('click', function () {
    $('.flash-message').hide();

    $resultsDisplay.show();
    $standingsDisplay.hide();
    $semifinalsDisplay.hide();
    $finalsDisplay.hide();
    $thisWeekDisplay.hide();
    $scheduleDisplay.hide();

    $resultsButton.addClass('active');
    $standingsButton.removeClass('active');
    $semifinalsButton.removeClass('active');
    $finalsButton.removeClass('active');
    $thisWeekButton.removeClass('active');
    $scheduleButton.removeClass('active');

    $resultsButton.removeClass('inactive');
    $standingsButton.addClass('inactive');
    $semifinalsButton.addClass('inactive');
    $finalsButton.addClass('inactive');
    $thisWeekButton.addClass('inactive');
    $scheduleButton.addClass('inactive');
});

$standingsButton.on('click', function () {
    $('.flash-message').hide();

    $resultsDisplay.hide();
    $standingsDisplay.show();
    $semifinalsDisplay.hide();
    $finalsDisplay.hide();
    $thisWeekDisplay.hide();
    $scheduleDisplay.hide();

    $resultsButton.removeClass('active');
    $standingsButton.addClass('active');
    $semifinalsButton.removeClass('active');
    $finalsButton.removeClass('active');
    $thisWeekButton.removeClass('active');
    $scheduleButton.removeClass('active');

    $resultsButton.addClass('inactive');
    $standingsButton.removeClass('inactive');
    $semifinalsButton.addClass('inactive');
    $finalsButton.addClass('inactive');
    $thisWeekButton.addClass('inactive');
    $scheduleButton.addClass('inactive');
});

$semifinalsButton.on('click', function () {
    $('.flash-message').hide();

    $resultsDisplay.hide();
    $standingsDisplay.hide();
    $semifinalsDisplay.show();
    $finalsDisplay.hide();
    $thisWeekDisplay.hide();
    $scheduleDisplay.hide();

    $resultsButton.removeClass('active');
    $standingsButton.removeClass('active');
    $semifinalsButton.addClass('active');
    $finalsButton.removeClass('active');
    $thisWeekButton.removeClass('active');
    $scheduleButton.removeClass('active');

    $resultsButton.addClass('inactive');
    $standingsButton.addClass('inactive');
    $semifinalsButton.removeClass('inactive');
    $finalsButton.addClass('inactive');
    $thisWeekButton.addClass('inactive');
    $scheduleButton.addClass('inactive');
});

$finalsButton.on('click', function () {
    $('.flash-message').hide();

    $resultsDisplay.hide();
    $standingsDisplay.hide();
    $semifinalsDisplay.hide();
    $finalsDisplay.show();
    $thisWeekDisplay.hide();
    $scheduleDisplay.hide();

    $resultsButton.removeClass('active');
    $standingsButton.removeClass('active');
    $semifinalsButton.removeClass('active');
    $finalsButton.addClass('active');
    $thisWeekButton.removeClass('active');
    $scheduleButton.removeClass('active');

    $resultsButton.addClass('inactive');
    $standingsButton.addClass('inactive');
    $semifinalsButton.addClass('inactive');
    $finalsButton.removeClass('inactive');
    $thisWeekButton.addClass('inactive');
    $scheduleButton.addClass('inactive');
});

$thisWeekButton.on('click', function () {
    $('.flash-message').hide();

    $resultsDisplay.hide();
    $standingsDisplay.hide();
    $semifinalsDisplay.hide();
    $finalsDisplay.hide();
    $thisWeekDisplay.show();
    $scheduleDisplay.hide();

    $resultsButton.removeClass('active');
    $standingsButton.removeClass('active');
    $semifinalsButton.removeClass('active');
    $finalsButton.removeClass('active');
    $thisWeekButton.addClass('active');
    $scheduleButton.removeClass('active');

    $resultsButton.addClass('inactive');
    $standingsButton.addClass('inactive');
    $semifinalsButton.addClass('inactive');
    $finalsButton.addClass('inactive');
    $thisWeekButton.removeClass('inactive');
    $scheduleButton.addClass('inactive');
});

$scheduleButton.on('click', function () {
    $('.flash-message').hide();

    $resultsDisplay.hide();
    $standingsDisplay.hide();
    $semifinalsDisplay.hide();
    $finalsDisplay.hide();
    $thisWeekDisplay.hide();
    $scheduleDisplay.show();

    $resultsButton.removeClass('active');
    $standingsButton.removeClass('active');
    $semifinalsButton.removeClass('active');
    $finalsButton.removeClass('active');
    $thisWeekButton.removeClass('active');
    $scheduleButton.addClass('active');

    $resultsButton.addClass('inactive');
    $standingsButton.addClass('inactive');
    $semifinalsButton.addClass('inactive');
    $finalsButton.addClass('inactive');
    $thisWeekButton.addClass('inactive');
    $scheduleButton.removeClass('inactive');
});

$adminLoginButton.on('click', function () {
    $adminLoginForm.show();
});

$loginCancel.on('click', function () {
    $adminLoginForm.hide();
});

$schedulerForm.on('click', function (evt) {
    const $target = $(evt.target);
    if ($target.hasClass('cancel-button')) {
        $schedulerForm.hide();
    }
});

$reportForm.on('click', function (evt) {
    const $target = $(evt.target);
    if ($target.hasClass('cancel-button')) {
        $reportForm.hide();
    }
});

$resultForm.on('click', function (evt) {
    const $target = $(evt.target);
    if ($target.hasClass('cancel-button')) {
        $resultForm.hide();
    } else if ($target.attr('id') === 'result-submit') {
        updateGame();
    }
});

$scoreForm.on('click', function (evt) {
    const $target = $(evt.target);
    if ($target.hasClass('cancel-button')) {
        $scoreForm.hide();
    } else if ($target.attr('id') === 'score-submit') {
        updatePlayer();
    }
});

$scheduleGameButton.on('click', async function (evt) {
    const $target = $(evt.target);
    const targetId = $target.attr('id');
    const gameId = parseInt(targetId.slice(targetId.indexOf('-') + 1));

    res = await axios.get(`${BASE_URL}/games/${gameId}`);
    const game = res.data;

    let scheduleBlock = '';
    if (game.schedule) {
        const schedule = game.schedule;
        const day = schedule.slice(0, 3);
        const date = schedule.slice(5, 7);
        const month = schedule.slice(8, 11);
        const hourUTC = schedule.slice(17, 19);
        const minuteUTC = schedule.slice(20, 22);

        const here = new Date();
        const offset = here.getTimezoneOffset();

        let minutes = parseInt(hourUTC) * 60 + parseInt(minuteUTC) - offset;

        let hourLocal = Math.floor(minutes / 60);
        let minuteLocal = minutes - (hourLocal * 60);
        let label = 'AM';

        if (hourLocal === 0) {
            hourLocal = 12;
        } else if (hourLocal === 12) {
            label = 'PM';
        } else if (hourLocal > 12) {
            hourLocal -= 12;
            label = 'PM';
        }

        if (hourLocal.toString().length === 1) {
            hourLocal = `0${hourLocal}`;
        }
        if (minuteLocal.toString().length === 1) {
            minuteLocal = `0${minuteLocal}`;
        }

        scheduleBlock = `<div class="row">
                <div class="col-12">
                    <small class="text-muted">${day} ${month} ${date}, ${hourLocal}:${minuteLocal} ${label}</small>
                </div>
            </div>`;
    }

    let buttonLabel = 'Schedule';
    if (game.schedule) {
        buttonLabel = 'Reschedule';
    }

    const html = `<h3>Schedule Game</h3>
        <div class="list-container">
            <ul class="list-group">
                <li class="list-group-item">
                    ${scheduleBlock}
                    <div class="row">
                        <div class="col-10">
                            <h6><span class="white">&nbsp;&nbsp;&nbsp;&nbsp;</span> <a href="${game.white.url}"
                                    target="_blank">${game.white.username}</a> <small
                                    class="text-muted">${game.white.rating}</small></h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-10">
                            <h6><span class="black">&nbsp;&nbsp;&nbsp;&nbsp;</span> <a href="${game.black.url}"
                                    target="_blank">${game.black.username}</a> <small
                                    class="text-muted">${game.black.rating}</small></h6>
                        </div>
                    </div>
                </li>
                <li class="list-group-item">
                    <form id="schedule-form" method="POST" action="/games/${game.id}/schedule">
                        <label for="date">Choose a date and time:</label>
                        <select name="date" required>
                            <option value="01-10">Sun Jan 10</option>
                            <option value="01-11">Mon Jan 11</option>
                            <option value="01-12">Tue Jan 12</option>
                            <option value="01-13">Wed Jan 13</option>
                            <option value="01-14">Thu Jan 14</option>
                            <option value="01-15">Fri Jan 15</option>
                            <option value="01-16">Sat Jan 16</option>
                            <option value="01-17">Sun Jan 17</option>
                            <option value="01-18">Mon Jan 18</option>
                            <option value="01-19">Tue Jan 19</option>
                            <option value="01-20">Wed Jan 20</option>
                            <option value="01-21">Thu Jan 21</option>
                            <option value="01-22">Fri Jan 22</option>
                            <option value="01-23">Sat Jan 23</option>
                            <option value="01-24">Sun Jan 24</option>
                        </select>,
                        <select name="hour" required>
                            <option value="01">01</option>
                            <option value="02">02</option>
                            <option value="03">03</option>
                            <option value="04">04</option>
                            <option value="05">05</option>
                            <option value="06">06</option>
                            <option value="07">07</option>
                            <option value="08">08</option>
                            <option value="09">09</option>
                            <option value="10">10</option>
                            <option value="11">11</option>
                            <option value="00">12</option>
                        </select> :
                        <select name="minute" required>
                            <option value="00">00</option>
                            <option value="01">01</option>
                            <option value="02">02</option>
                            <option value="03">03</option>
                            <option value="04">04</option>
                            <option value="05">05</option>
                            <option value="06">06</option>
                            <option value="07">07</option>
                            <option value="08">08</option>
                            <option value="09">09</option>
                            <option value="10">10</option>
                            <option value="11">11</option>
                            <option value="12">12</option>
                            <option value="13">13</option>
                            <option value="14">14</option>
                            <option value="15">15</option>
                            <option value="16">16</option>
                            <option value="17">17</option>
                            <option value="18">18</option>
                            <option value="19">19</option>
                            <option value="20">20</option>
                            <option value="21">21</option>
                            <option value="22">22</option>
                            <option value="23">23</option>
                            <option value="24">24</option>
                            <option value="25">25</option>
                            <option value="26">26</option>
                            <option value="27">27</option>
                            <option value="28">28</option>
                            <option value="29">29</option>
                            <option value="30">30</option>
                            <option value="31">31</option>
                            <option value="32">32</option>
                            <option value="33">33</option>
                            <option value="34">34</option>
                            <option value="35">35</option>
                            <option value="36">36</option>
                            <option value="37">37</option>
                            <option value="38">38</option>
                            <option value="39">39</option>
                            <option value="40">40</option>
                            <option value="41">41</option>
                            <option value="42">42</option>
                            <option value="43">43</option>
                            <option value="44">44</option>
                            <option value="45">45</option>
                            <option value="46">46</option>
                            <option value="47">47</option>
                            <option value="48">48</option>
                            <option value="49">49</option>
                            <option value="50">50</option>
                            <option value="51">51</option>
                            <option value="52">52</option>
                            <option value="53">53</option>
                            <option value="54">54</option>
                            <option value="55">55</option>
                            <option value="56">56</option>
                            <option value="57">57</option>
                            <option value="58">58</option>
                            <option value="59">59</option>
                        </select>
                        <select name="am-pm" required>
                            <option value="AM">AM</option>
                            <option value="PM">PM</option>
                        </select><br>
                        <div class="schedule-button-container">
                            <button type="submit"
                                class="btn btn-outline-secondary schedule-button">${buttonLabel}</button>
                            <button type="button" class="btn btn-outline-danger cancel-button">Cancel</button>
                        </div>
                    </form>
                </li>
            </ul>
        </div>`;

    $schedulerForm.html(html);
    $schedulerForm.show();
});

$reportGameButton.on('click', async function (evt) {
    const $target = $(evt.target);
    const targetId = $target.attr('id');
    const gameId = parseInt(targetId.slice(targetId.indexOf('-') + 1));

    const html = `<div class="list-container">
            <h3>Report a Game</h3>
            <ul class="list-group">
                <li class="list-group-item">
                    <small>Just copy and paste the game URL and click 'Submit' and the admin will update
                        the page by the end of the
                        week.</small><br><br>
                    <form id="game-report-form" action="/games/${gameId}/report" method="POST">
                        <label for="url">Enter game URL:</label>
                        <input type="text" id="url" name="url" required><br>
                        <div class="schedule-button-container">
                            <button type="submit" class="btn btn-outline-success schedule-button">Submit</button>
                            <button type="button" class="btn btn-outline-danger cancel-button">Cancel</button>
                        </div>
                    </form>
                </li>
            </ul>
        </div>`;

    $reportForm.html(html);
    $reportForm.show();
});

$resultButton.on('click', function (evt) {
    $target = $(evt.target);
    const targetId = $target.attr('id');
    const gameId = parseInt(targetId.slice(targetId.indexOf('-') + 1));

    const html = `<h3>Enter Result</h3>
        <form id="add-result-form">
            <p>Game <span id="game-id">${gameId}</span></p>
            <label for="result">Result:</label>&nbsp;
            <input type="text" id="result" name="result" required><br>
            <div class="schedule-button-container">
                <button type="button" id="result-submit" class="btn btn-outline-secondary schedule-button">Submit</button>
                <button type="button" id="result-cancel" class="btn btn-outline-danger cancel-button">Cancel</button>
            </div>
        </form>`;

    $resultForm.html(html);
    $resultForm.show();
});

async function updateGame() {
    const resultStr = $('#result').val();
    const gameId = parseInt($('#game-id').text());

    let result = '';
    if (resultStr === '1-0') {
        result = 'W';
    } else if (resultStr === '0-1') {
        result = 'B';
    } else if (resultStr === '0.5-0.5') {
        result = 'D';
    } else if (resultStr === '0-0') {
        result = 'DF';
    } else {
        result = 'yeet_mcgeet';
    }

    const res = await axios.post(`${BASE_URL}/games/${gameId}/${result}`);
    let status = res.data.status;

    if (status === 'success') {
        $resultForm.hide();
        $(`#result-container-${gameId}`).html(`<small>${resultStr}</small>`);
    } else {
        console.log('try again lol');
    }
}

$scoreButton.on('click', function (evt) {
    const $target = $(evt.target);
    const targetId = $target.attr('id');
    const playerId = parseInt(targetId.slice(targetId.indexOf('-') + 1));

    const html = `<h3>Update Score</h3>
        <form id="update-score-form">
            <p>Player <span id="player-id">${playerId}</span></p>
            <label for="score">New score:</label>&nbsp;
            <input type="text" id="score" name="score" required><br>
            <div class="schedule-button-container">
                <button type="button" id="score-submit" class="btn btn-outline-secondary schedule-button">Submit</button>
                <button type="button" id="score-cancel" class="btn btn-outline-danger cancel-button">Cancel</button>
            </div>
        </form>`;

    $scoreForm.html(html);
    $scoreForm.show();
});

async function updatePlayer() {
    const scoreStr = $('#score').val();
    const playerId = $('#player-id').text();
    const tournamentId = $('#tournament-id').text();

    const score = Math.floor(parseFloat(scoreStr) * 100);

    const res = await axios.post(`${BASE_URL}/players/${playerId}/${tournamentId}/${score}`);
    const status = res.data.status;

    if (status === 'success') {
        $scoreForm.hide();
        $(`#score-container-${playerId}`).text(scoreStr);
        $(`#rating-container-${playerId}`).text(res.data.new_rating);
    } else {
        console.log('try again lol');
    }
}