const sections = document.getElementsByTagName('section')

let index_game_list = null
let index_highlight = null
let index_destaque = null
let index_top_globo = null
let section = null

for (let i=0; i < sections.length;i++) 
{ 
    section = sections[i].getAttribute("class")

    switch (section) {
        case 'regua-de-jogos hui-container':
            index_game_list = i
            break
        case 'highlight-container hui-container':
            index_highlight = i
            break
        case 'destaque-trilho hui-container':
            index_destaque = i
            break
        case 'area-top-globo hui-container':
            index_top_globo = i
            break
    }
}

const game_list = sections[index_game_list]
const highlights = sections[index_highlight]
const destaques = sections[index_destaque]
const top_globo = sections[index_top_globo]

const topicos_top_globo = top_globo.getElementsByClassName("topglobocom__ranking__container")


let jogos = game_list.getElementsByTagName('a')
let link = jogos[0].href
let title = jogos[0].getElementsByTagName('h5')[0].innerText
let times = jogos[0].getElementsByClassName("regua-jogos__teamscore")
let nomeTime = times[0].getElementsByClassName("regua-jogos__teamname")[0].getElementsByTagName('h3')[0].innerText
let gols = times[0].getElementsByClassName("regua-jogos__score")[0].getElementsByTagName('span')[0].innerText