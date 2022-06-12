import React from 'react'
import Login from './Login'
import useLocalStorage from '../hooks/useLocalStorage';
import Dashboard from './Dashboard'
import { ContactsProvider } from '../contexts/ContactsProvider'
import { ConversationsProvider } from '../contexts/ConversationsProvider';
import { SocketProvider } from '../contexts/SocketProvider';

function App() {
  const [token, setToken] = useLocalStorage('token')

  const dashboard = (
    <Dashboard token={token} />
  )

  return (
    token ? dashboard : <Login onIdSubmit={setToken} />
  )
}

export default App;