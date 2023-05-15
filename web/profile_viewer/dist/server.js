const express = require('express')
const session = require('express-session')

const app = express()
app.use(express.urlencoded({
    extended: true
}))
app.use(express.static('public'))
app.use(session({
    resave: false,
    saveUninitialized: false,
    secret: require('node:crypto').randomBytes(32).toString('base64')
}))

// this is flag
const secretFlag = process.env.FLAG ?? 'TSGLIVE{DUMMY}'

function getUsers() {
    return {
        alice: { name: 'Alice Anderson' },
        bob: { name: 'Bob Baker' },
        carol: { name: 'Carol Carlson' },
        dave: { name: 'Dave Dixon' },
        eve: { name: 'Eve Eaton' }
    }
}

app.get('/profile', (req, res) => {
    const profile = JSON.parse(req.session.data ?? '{ "profile": {} }').profile
    res.json({
        secret: profile[secretFlag],
        name: profile.name
    })
})

app.post('/profile', (req, res) => {
    const name = req.body.name
    if (name.length > 5) {
        res.send('codename too long')
        return
    }
    const profile = getUsers()[name]
    if (profile == null || typeof profile.name !== 'string') {
        res.send('Unknown codename')
        return
    }
    profile[secretFlag] = 'personal data'
    req.session.data = JSON.stringify({ profile })
    res.send('ok')
})

app.listen(3456, () => {
    console.log(`Example app listening on port 3456`)
})
